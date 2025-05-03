import os
import time
import shutil
import frontmatter

CWD = os.path.dirname(os.path.abspath(__file__))

SOURCE_DIR = CWD
DEST_DIR = os.path.join(CWD, "posts")

yaml_header = """---
title: "{}"
date: {}
series: 
- "{}"
---

"""

def walk_md(path):
    if os.path.basename(path)[0] == '.':
        return
    if os.path.isdir(path):
        if os.path.basename(path) == "posts":
            return
        dir_dest = os.path.join(DEST_DIR, path[len(SOURCE_DIR) + 1:])
        os.mkdir(dir_dest)
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            walk_md(filepath)
        return
    md_filename = os.path.basename(path)
    if not md_filename.endswith(".md"):
        return

    title = md_filename[:-3]
    date = time.strftime("%Y-%m-%d", time.localtime(os.stat(path).st_ctime))
    post_series = os.path.basename(os.path.dirname(path))
    print("- " + title)

    post = frontmatter.load(path)
    if not md_filename.endswith("index.md"):
        post['title'] = title
        post['date'] = date
        post['series'] = [post_series]
    
    md_dest = os.path.join(DEST_DIR, path[len(SOURCE_DIR) + 1:])
    print(md_dest)
    frontmatter.dump(post, md_dest)


if __name__ == "__main__":
    # 如果目标文件夹存在，就把它删掉
    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)

    walk_md(SOURCE_DIR)

    print("Generation over!")
