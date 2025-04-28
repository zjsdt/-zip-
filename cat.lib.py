from logging import shutdown

code="zjsdt"
sudo={ord(i) for i in code}

sudo = ''.join(map(str, sorted(sudo)))
print(sudo)
a=input("请输入密钥(密码如上所示)：")
print(a)
if a==sudo:
    CAT_ASCII =r"""
     /\_/\
    ( o.o ) 
     > ^ <
    /  -  \ 
    \_____/ 
      | |   
     /   \ 
    """

# 在库初始化时调用
    def show_welcome():
        print("\033[36m")  # 青色
        print(CAT_ASCII)
        print(" Welcome to CatLib! ")
        print("\033[0m")
        # 使用示例
    if __name__ == "__main__":
        show_welcome()

    import zipfile
    import os


    path=input(r"请输入压缩包和密码本所在的路径（路径需要相同）：")
    zip = input("请输入在电脑桌面路径的zip压缩包：")
    txt = input("请输入在电脑桌面路径的密码本（txt类型）：")
    extract_dir = "C:\\Users\\asu\\pjj"
    desktop_path = os.path.join(os.path.expanduser(path))  # 自动获取桌面路径
    file_path = os.path.join(desktop_path, txt)  # 拼接完整文件路径
    zip_path = os.path.join(desktop_path, zip)  # 拼接完整压缩包路径 :ml-citation{ref="6" data="citationList"}




    # 定义桌面文件路径（跨平台兼容）
    def mimaben():
        file_path = os.path.join(desktop_path, txt)  # 拼接完整文件路径
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())# 去除行首尾空白符（包括换行符）
                    password =line.strip()  # 用户输入密码（字符串类型）
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            zip_ref.extractall(extract_dir, pwd=password.encode('utf-8'))  # 确保密码转为字节
                        print("解压成功！")
                        exit(0)
                    except RuntimeError:
                        print("密码错误或文件损坏！")
                    except FileNotFoundError:
                        print("ZIP 文件不存在！")
                        exit(0)
        except FileNotFoundError:
            print(f"错误：文件 {file_path} 不存在！")
        except UnicodeDecodeError:
            print(f"错误：文件 {file_path} 编码不兼容（请尝试其他编码格式，如 gbk）")
        except Exception as e:
            print(f"未知错误：{e}")


    mimaben()


else:
    print("bad boy")
    shutdown()
input('按enter键结束')