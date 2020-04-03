
#include "batt.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int set_batt_from_ports(batt_t *batt){
  if(BATT_VOLTAGE_PORT < 0){
    return 1;
  }
  batt->volts = BATT_VOLTAGE_PORT;
  batt->percent = (BATT_VOLTAGE_PORT-3000)/8;
  batt->mode = BATT_STATUS_PORT & 1;
  if(BATT_VOLTAGE_PORT>3800){
    batt->percent = 100;
  }
  else if(BATT_VOLTAGE_PORT<3000){
    batt->percent = 0;
  }
  return 0;



  return 0;
}

int set_display_from_batt(batt_t batt, int *display){
  int masks[11] = {0b0111111,0b0000011,0b1101101,0b1100111,0b1010011,0b1110110,0b1111110,0b0100011,0b1111111,0b1110111,0b0000000};
  int extra = batt.volts % 10;
  int right = (batt.volts % 100 - extra) / 10;
  int middle = (batt.volts % 1000 - right*10 - extra)/100;
  int left = (batt.volts - middle*100 - right*10 - extra)/1000;
  if(extra >= 5){
    right += 1;
  }
  if(right>9){
    right = 0;
    middle += 1;
  }
  int res = 0;
  int lvl=0;
  if (batt.percent < 5){
    lvl = 0;
  }
  else if (batt.percent < 30 && batt.percent>=5){
    lvl = 0b10000;
  }
  else if(batt.percent>=30 && batt.percent<50){
    lvl = 0b11000;
  }
  else if(batt.percent>=50 && batt.percent<70){
    lvl = 0b11100;
  }
  else if(batt.percent>=70 && batt.percent<=90){
    lvl = 0b11110;
  }
  else{
    lvl = 0b11111;
  }
  if(batt.mode == 0)/*for volts*/{
    int sig = 0b011;
    res += (lvl<<24) + (sig<<21) + (masks[left]<<14) + (masks[middle]<<7) + masks[right];
    *display = res;
    return 0;
  }
  int pright; int pmiddle; int pleft; int sig = 0b100;
  if(batt.percent==100){
    pright = 0;
    pmiddle = 0;
    pleft = 1;
  }
  else if(batt.percent<100 && batt.percent >=10){
    pright = batt.percent%10;
    pmiddle = (batt.percent - pright) / 10;
    pleft = 10;
  }
  else{
    pright = batt.percent;
    pmiddle = 10;
    pleft = 10;
  }
  res += (lvl<<24) + (sig<<21) + (masks[pleft]<<14) + (masks[pmiddle]<<7) + masks[pright];
  *display = res;
  return 0;
}

int batt_update(){
  batt_t batt;
  int display = 0;
  int res = set_batt_from_ports(&batt);
  int res1 = set_display_from_batt(batt,&display);
  if(res!=0 || res1!=0){
    return 1;
  }
  BATT_DISPLAY_PORT = display;
  return 0;
}
