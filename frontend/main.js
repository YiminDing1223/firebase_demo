// 1. Firebase config
const firebaseConfig = {
  apiKey: "AIzaSyDto3e1D9DfVXcb3675W2xCe164YHj-vJ4", 
  authDomain: "practice-e2b0c.firebaseapp.com",
  projectId: "practice-e2b0c",
  storageBucket: "practice-e2b0c.appspot.com",
  messagingSenderId: "996740517187",
  appId: "1:996740517187:web:9b3d032651b87354f533f6"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();


// 2. DOM elements
const loginSection = document.getElementById("login-section");
const contentSection = document.getElementById("content-section");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const loginBtn = document.getElementById("loginBtn");
const getLineBtn = document.getElementById("getLineBtn");
const lineDisplay = document.getElementById("lineDisplay");
const logoutBtn = document.getElementById("logoutBtn");

// 3. Backend API base URL (local for now)
const BACKEND_URL = "http://127.0.0.1:8080";

// 4. Login with email & password
loginBtn.addEventListener("click", async () => {
  const email = emailInput.value;
  const password = passwordInput.value;

  try {
    await auth.signInWithEmailAndPassword(email, password);
    alert("Logged in!");
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
});

// 5. Listen for auth state changes
auth.onAuthStateChanged((user) => {
  if (user) {
    // Logged in
    loginSection.style.display = "none";
    contentSection.style.display = "block";
  } else {
    // Logged out
    loginSection.style.display = "block";
    contentSection.style.display = "none";
  }
});

// 6. Logout
logoutBtn.addEventListener("click", async () => {
  await auth.signOut();
});

// 7. Fetch user's line from backend
getLineBtn.addEventListener("click", async () => {
  const user = auth.currentUser;
  if (!user) {
    alert("Not logged in.");
    return;
  }

  const userId = user.uid; // Firebase user ID

  try {
    const res = await fetch(`${BACKEND_URL}/line?user_id=${encodeURIComponent(userId)}`);
    const data = await res.json();
    lineDisplay.textContent = data.text;
  } catch (err) {
    console.error(err);
    lineDisplay.textContent = "Error fetching line.";
  }
});
