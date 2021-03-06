#!/usr/bin/env python3

# Character escaping:
# escaping ist eine Möglichkeit Zeichen und Steuerzeichen (z.B. \n und \t) in einen
# String einzubauen
print("Tab:\t#")

# Das Zeichen hinter einem \ wird entweder Steuerzeichen interpretiert oder ignoriert
print("\aabc")

# Folglich kann ein \ nicht trivial in einen String gepackt werden:
# Nicht so:
print("\0/")
# Sondern so:
print("\\0/")

# Rawstrings können kein escaping:
print(r"\n")
print(r"\0/")


# string.format()
print("Das folgende Wort wird ersetzt: '{}' Der Rest nicht.".format("blargh"))
# Auch:
print("Das folgende Wort wird ersetzt: '{0} und {1}' Der Rest nicht.".format("foo", "bar"))

# String.split()
s = "a;b;cd"
l = s.split(";")
print(repr(l))
# l entspricht nun: ["a", "b", "cd"]
# Geeignet zum Parsen von .csv Dateien zum Beispiel

s = ";".join(l)
# l enspricht nun: 'a;b;cd'

# Wiederholung: 
# string.split(char) Trennt den String bei jedem Auftreten von char
# string.join(list) Trennt die Liste mit String und gibt einen String zurück
