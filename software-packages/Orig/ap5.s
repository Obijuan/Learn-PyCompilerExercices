                                @ ap5.s
          .text                 @ start of read-only segment
          .global _start
_start:
          ldr r0, x             @ does not work
          mov r7, #1
          svc 0

          .data                 @ start of read/write segment
x:        .word 5               @ the variable x
