#! /usr/bin/env nix-shell
#! nix-shell -i python3.11 -p python311 python311Packages.prettytable

import prettytable

# Print a simple table.
t = prettytable.PrettyTable(["N", "N^2"])

for n in range(1, 10):
    t.add_row([n, n * n])
print(t)
