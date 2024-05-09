          .global f
          .data
x:        .word 7
f:        ldr r0, x
          mov pc, lr
