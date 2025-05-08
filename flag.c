#include <stdio.h>
#include <stdint.h>

void printFlag(void)

{
    uint8_t local_88 [107];
    uint8_t local_1d;
  int local_1c;
  int local_18;
  int local_14;
  int local_10;
  int local_c;
  
  local_88[0] = 0xe3;
  local_88[1] = 0xe9;
  local_88[2] = 0xf1;
  local_88[3] = 0xf2;
  local_88[4] = 0xf8;
  local_88[5] = 0xec;
  local_88[6] = 0xfb;
  local_88[7] = 0xe8;
  local_88[8] = 0xf1;
  local_88[9] = 0xc1;
  local_88[10] = 0xec;
  local_88[0xb] = 0xfb;
  local_88[0xc] = 0xf8;
  local_88[0xd] = 0xf8;
  local_88[0xe] = 0xeb;
  local_88[0xf] = 0xfc;
  local_88[0x10] = 0xc1;
  local_88[0x11] = 0xf1;
  local_88[0x12] = 0xea;
  local_88[0x13] = 0xc1;
  local_88[0x14] = 0xfb;
  local_88[0x15] = 0xe8;
  local_88[0x16] = 0xf7;
  local_88[0x17] = 0xf2;
  local_88[0x18] = 0xc1;
  local_88[0x19] = 0xf9;
  local_88[0x1a] = 0xf0;
  local_88[0x1b] = 0xf1;
  local_88[0x1c] = 0xf2;
  local_88[0x1d] = 0xe5;
  local_88[0x1e] = 0xd9;
  local_88[0x1f] = 0xdf;
  local_88[0x20] = 0xd2;
  local_88[0x21] = 0xd8;
  local_88[0x22] = 0;
  local_88[0x23] = 0;
  local_88[0x24] = 0;
  local_88[0x25] = 0;
  local_88[0x26] = 0;
  local_88[0x27] = 0;
  local_88[0x28] = 0;
  local_88[0x29] = 0;
  local_88[0x2a] = 0;
  local_88[0x2b] = 0;
  local_88[0x2c] = 0;
  local_88[0x2d] = 0;
  local_88[0x2e] = 0;
  local_88[0x2f] = 0;
  local_88[0x30] = 0;
  local_88[0x31] = 0;
  local_88[0x32] = 0;
  local_88[0x33] = 0;
  local_88[0x34] = 0;
  local_88[0x35] = 0;
  local_88[0x36] = 0;
  local_88[0x37] = 0;
  local_88[0x38] = 0;
  local_88[0x39] = 0;
  local_88[0x3a] = 0;
  local_88[0x3b] = 0;
  local_88[0x3c] = 0;
  local_88[0x3d] = 0;
  local_88[0x3e] = 0;
  local_88[0x3f] = 0;
  local_88[0x40] = 0;
  local_88[0x41] = 0;
  local_88[0x42] = 0;
  local_88[0x43] = 0;
  local_88[0x44] = 0;
  local_88[0x45] = 0;
  local_88[0x46] = 0;
  local_88[0x47] = 0;
  local_88[0x48] = 0;
  local_88[0x49] = 0;
  local_88[0x4a] = 0;
  local_88[0x4b] = 0;
  local_88[0x4c] = 0;
  local_88[0x4d] = 0;
  local_88[0x4e] = 0;
  local_88[0x4f] = 0;
  local_88[0x50] = 0;
  local_88[0x51] = 0;
  local_88[0x52] = 0;
  local_88[0x53] = 0;
  local_88[0x54] = 0;
  local_88[0x55] = 0;
  local_88[0x56] = 0;
  local_88[0x57] = 0;
  local_88[0x58] = 0;
  local_88[0x59] = 0;
  local_88[0x5a] = 0;
  local_88[0x5b] = 0;
  local_88[0x5c] = 0;
  local_88[0x5d] = 0;
  local_88[0x5e] = 0;
  local_88[0x5f] = 0;
  local_88[0x60] = 0;
  local_88[0x61] = 0;
  local_88[0x62] = 0;
  local_88[99] = 0;
  for (local_c = 0; local_88[local_c] != 0; local_c = local_c + 1) {
  }
  for (local_10 = 0; local_10 < local_c / 2; local_10 = local_10 + 1) {
    local_1d = local_88[local_10];
    local_88[local_10] = local_88[(local_c - local_10) + -1];
    local_88[(local_c - local_10) + -1] = local_1d;
  }
  for (local_14 = 0; local_14 < local_c; local_14 = local_14 + 1) {
    local_88[local_14] = local_88[local_14] ^ 0x61;
  }
  for (local_18 = 0; local_18 < local_c; local_18 = local_18 + 1) {
    local_88[local_18] = ~local_88[local_18];
  }
  for (local_1c = 0; local_1c < local_c; local_1c = local_1c + 1) {
    putchar((int)(char)local_88[local_1c]);
  }
  return;
}

int main(int argc, char *argv[])
{
  printFlag();
  return 0;
}