BYTES_PER_KIB = 1024
file_size_bytes = int(input("File size in bytes: "))
size_kib = file_size_bytes / BYTES_PER_KIB 
size_mib = file_size_bytes / BYTES_PER_KIB ** 2
size_gib = file_size_bytes / BYTES_PER_KIB ** 3
print(f"Size in KiB: {size_kib:,.2f}")
print(f"Size in MiB: {size_mib:,.2f}")
print(f"Size in GiB: {size_gib:,.2f}")
