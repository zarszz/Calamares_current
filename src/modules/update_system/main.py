#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Made by fernandomaroto for EndeavourOS and Portergos.
# Should work in any arch-based distros
# Trying K.I.S.S filosophy

import subprocess
import libcalamares

root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

def update_db():

    START_HAVEGED = "haveged -w 1024"
    PACMAN_INIT = "pacman-key --init"
    PACMAN_POPULATE = "pacman-key --populate"
    PACMAN_REFRESH ="pacman-key --refresh-keys"
    STOP_HAVEGED = "pkill haveged"
    BACKUP_MIRROLIST = "cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak"
    BEST_MIRRORS = "reflector --verbose --age 8 --fastest 128 --latest 64 --number 32 --sort rate --save /etc/pacman.d/mirrorlist"
    PACMAN_UPDATE = "pacman -Syu --noconfirm"

    # Populate and refresh keys
    subprocess.call(['chroot'] + [root_mount_point] + START_HAVEGED.split(' ')) 
    subprocess.call(['chroot'] + [root_mount_point] + PACMAN_INIT.split(' '))  
    subprocess.call(['chroot'] + [root_mount_point] + PACMAN_POPULATE.split(' ')) 
    subprocess.call(['chroot'] + [root_mount_point] +  PACMAN_REFRESH.split(' '))
    subprocess.call(['chroot'] + [root_mount_point] + STOP_HAVEGED.split(' '))   
    # Best mirrors
    subprocess.call(['chroot'] + [root_mount_point] + BACKUP_MIRROLIST.split(' '))  
    subprocess.call(['chroot'] + [root_mount_point] + BEST_MIRRORS.split(' '))
    # Update
    subprocess.call(['chroot'] + [root_mount_point] + PACMAN_UPDATE.split(' '))

def run():
    # Check internet
    if libcalamares.globalstorage.value("hasInternet"):
        try:
            update_db()
        except:
            pass





   
