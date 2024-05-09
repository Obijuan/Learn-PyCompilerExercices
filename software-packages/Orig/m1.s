          .global _start
_start:
          bl  f
          mov r7, #1
          svc 0
