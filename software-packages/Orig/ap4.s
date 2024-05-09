                                @ ap4.s
          .text                 @ start of read-only segment
          .global _start
_start:                         @ address
          ldr r0, [pc, #4]      @ 8000
          mov r7, #1            @ 8004
          svc 0                 @ 8008

x:        .word 14              @ 8012