# Generate vectors.S, the trap/interrupt entry points.
# There has to be one entry point per interrupt number
# since otherwise there's no way for trap() to discover
# the interrupt number.

print("# generated by vectors.pl - do not edit")
print("# handlers")
print(".global alltraps")
for i in range(256):
    print(".global vector{}".format(i))
    print("vector{}:".format(i))
    if not (i == 8 or (i >= 10 and i <= 14) or i == 17):
        print("    pushl $0")
    print("    pushl ${}".format(i))
    print("    jmp alltraps\n")

print("\n# vector table")
print(".data")
print(".global vectors")
print("vectors:")
for i in range(256):
    print("    .long vector{}".format(i))
