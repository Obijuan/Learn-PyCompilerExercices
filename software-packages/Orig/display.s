                            @ display.s
          .global main      @ printf assumed global
          .main
          .text             @ start of read-only segment
main:     push {lr}         @ save lr by pushing onto stack

          ldr r0, =.fmt0    @ get address of string
          ldr r1, =x        @ get address of x
          ldr r1, [r1]      @ get value of x
          bl  printf        @ call printf

          pop {pc}          @ pop saved lr into pc
          .data             @ start of read/write segment
.fmt0:    .asciz "x = %d\n" @ null-terminated ASCII string
x:        .word 27
