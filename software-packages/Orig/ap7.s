                                @ ap7.s
          .text                 @ start of read-only segment
          .global _start
_start:
          ldr r0, =x            @ load address of x
          ldr r0, [r0]          @ load r0 from address in r0
          mov r7, #1
          svc 0
                                @ literal pool is here

          .data                 @ start of read/write segment
x:        .word 67              @ variable x
