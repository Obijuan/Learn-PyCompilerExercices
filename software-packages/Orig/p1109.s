          .text
          .global _start
_start:
          ldr r0, =a
          ldr r0, [r0]
          mov r7, #1
          svc 0
          .space 20000
          .data
a:        .word 17
