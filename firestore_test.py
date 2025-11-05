import os
from google.cloud import firestore

# 🔑 设置服务账号密钥路径（和这个文件在同一个文件夹里）
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "practice-e2b0c-firebase-adminsdk-fbsvc-6ed393b5fe.json"

# 🚀 初始化 Firestore 客户端
db = firestore.Client()

# ========== 1️⃣ 新增两个用户 ==========
print("\n1️⃣ Adding new users...")
user1_ref = db.collection("users").document("user1")
user1_ref.set({
    "name": "Yimin",
    "role": "student",
    "age": 25
})

user2_ref = db.collection("users").document("user2")
user2_ref.set({
    "name": "Alex",
    "role": "engineer",
    "age": 30
})

print("✅ Added user1 and user2")

# ========== 2️⃣ 读取所有用户 ==========
print("\n2️⃣ Reading all users from Firestore...")
users_ref = db.collection("users").stream()

for user in users_ref:
    print(f"📄 {user.id} => {user.to_dict()}")

# ========== 3️⃣ 更新字段（修改 user1 的 age） ==========
print("\n3️⃣ Updating age for user1...")
db.collection("users").document("user1").update({"age": 26})
updated_user = db.collection("users").document("user1").get()
print("✅ Updated user1:", updated_user.to_dict())

# ========== 4️⃣ 删除一个文档 ==========
print("\n4️⃣ Deleting user2...")
db.collection("users").document("user2").delete()
print("✅ user2 deleted")

# ✅ 最终查看剩余文档
print("\nRemaining users:")
for user in db.collection("users").stream():
    print(f"📄 {user.id} => {user.to_dict()}")

print("\n🎉 All Firestore operations completed successfully!")
