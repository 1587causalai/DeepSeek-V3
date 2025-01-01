import os
import glob

def add_answer_link(task_file):
    # 读取原文件内容
    with open(task_file, 'r', encoding='utf-8') as f:
        content = f.read().rstrip()
    
    # 构造对应的readme路径
    dir_path = os.path.dirname(task_file)
    answer_path = f"/{dir_path}/readme.md"
    
    # 检查是否已经有答案链接
    if "## 参考答案" not in content:
        # 添加答案链接
        answer_section = f"\n\n---\n\n## 参考答案\n👉 [点击查看参考答案]({answer_path})\n"
        content += answer_section
        
        # 写回文件
        with open(task_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added answer link to {task_file}")
    else:
        print(f"Answer section already exists in {task_file}")

def main():
    # 找到所有的task.md文件
    task_files = glob.glob("Tutorial/docs/**/task.md", recursive=True)
    
    for task_file in task_files:
        add_answer_link(task_file)
        
if __name__ == "__main__":
    main() 