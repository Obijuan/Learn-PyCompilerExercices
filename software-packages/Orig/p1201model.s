@ p1201model.s
          .global main       @ scanf and printf assumed global 
          .data              @ start of read/write segment
main:
          push {lr}          @ save lr by pushing onto stack
          
          ldr r0, =.z0       @ display prompt message
          bl printf

          ldr r0, =.z1       @ get address of string
          ldr r1, =x         @ get address of x
          bl scanf           @ call scanf, value goes into x

          ldr r0, =.z1        
          ldr r1, =y
          bl scanf           @ call scanf, value goes into y

          ldr r0, =.z1
          ldr r1, =z
          bl scanf           @ call scanf, value goes into z
 
          ldr r0, x          @ get x
          ldr r1, y          @ get y
          add r0, r0, r1     @ add x and y, result into r0
          ldr r1, z          @ get z
          add r1, r0, r1     @ add z to previous sum


          ldr r0, =.z2       @ get address of string
          bl  printf         @ call printf
 
          pop {pc}           @ pop saved lr into pc

.z0:      .asciz "enter 3 integers\n"
.z1:      .asciz "%d"        @ null-terminated ASCII string
.z2:      .asciz "sum = %d\n"      @ null-terminated ASCII string
x:        .word 0
y:        .word 0
z:        .word 0

