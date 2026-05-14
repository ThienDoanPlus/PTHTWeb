#!/bin/bash
read -p "Nhap ten may moi: " moi
read -p "Ban co chac chan muon doi hay khong? (Yes/No): " check

if [ "$check" == "Yes" ]; then
    sudo hostnamectl set-hostname "$moi"
    echo "Da doi ten may. Ban nen khoi dong lai de co hieu luc."
    read -p "Khoi dong lai ngay? (Yes/No): " rb
    if [ "$check" == "Yes" ]; then sudo reboot; fi
else
    echo "Ten may hien tai la: $(hostname)"
fi
