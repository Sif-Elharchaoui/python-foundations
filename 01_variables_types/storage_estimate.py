BYTES_PER_MIB = 1024 ** 2

file_count = int(input("Number of files: "))
average_size_mib = float(input("Average size per file in MiB: "))

total_size_mib = average_size_mib * file_count 
total_size_bytes =  BYTES_PER_MIB*  total_size_mib
total_size_gib = total_size_mib / 1024


print(f"Total storage in MiB: {total_size_mib:,.2f}")
print(f"Total storage in bytes: {total_size_bytes:,.0f}")
print(f"Storage in GiB: {total_size_gib:.2f}")
