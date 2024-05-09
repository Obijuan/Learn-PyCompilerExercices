                                @ ap6.s
          .text                 @ start of read-only segment
          .global _start
_start:
          ldr r0, ax            @ load address of x
          ldr r0, [r0]          @ load r0 from address in r0
          mov r7, #1
          svc 0
ax:       .word x               @ label x is symbolic address          

          .data                 @ start of read/write segment
x:        .word 67              @ the variable x
