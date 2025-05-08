/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>


void FUN_08049150(int param_1)
{
  putchar(param_1);
  return;
}

void print_safe_contents(void)
{
    int in_GS_OFFSET;
  uint8_t *local_30;
  uint8_t local_28 [24];
  uint8_t local_28 [24];
  int local_10;
  
  local_10 = *(int *)(in_GS_OFFSET + 0x14);
  local_28[0] = 0xbc;
  local_28[1] = 0xbc;
  local_28[2] = 0xb6;
  local_28[3] = 0xab;
  local_28[4] = 0x84;
  local_28[5] = 0x98;
  local_28[6] = 0x9b;
  local_28[7] = 0x9d;
  local_28[8] = 0xa0;
  local_28[9] = 0x8b;
  local_28[10] = 0xcf;
  local_28[0xb] = 0xa0;
  local_28[0xc] = 0x8b;
  local_28[0xd] = 0x97;
  local_28[0xe] = 0xcc;
  local_28[0xf] = 0xa0;
  local_28[0x10] = 0x8d;
  local_28[0x11] = 0x9a;
  local_28[0x12] = 0xca;
  local_28[0x13] = 0x9c;
  local_28[0x14] = 0x8a;
  local_28[0x15] = 0x9a;
  local_28[0x16] = 0x82;
  local_28[0x17] = 0xff;
  while( 1 ) {
  while( true ) {
    if ((uint8_t)~*local_30 == 0) break;
    FUN_08049150(~*local_30);
    local_30 = local_30 + 1;
  }
  FUN_08049150(10);
  if (local_10 != *(int *)(in_GS_OFFSET + 0x14)) {
    __stack_chk_fail_local();
  }
  return;
}