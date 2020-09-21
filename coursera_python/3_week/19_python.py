v_a = str(input())
v_b = v_a[v_a.find("h") + 1:v_a.rfind("h")]
print(v_a[0:v_a.find("h")]+"h",
      v_b.replace("h", "H"),
      v_a[v_a.rfind("h")::], sep="")
