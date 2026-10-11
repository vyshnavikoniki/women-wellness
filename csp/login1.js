document
    .getElementById("loginForm")
    .addEventListener("submit", function(event) {

        event.preventDefault();


        // Get entered values

        const email =
            document.getElementById("email").value.trim();

        const password =
            document.getElementById("password").value;


        // Error message element

        const errorMessage =
            document.getElementById("errorMessage");


        // Get registered user

        const storedUser =
            localStorage.getItem("womenWellAIUser");


        // Check whether account exists

        if (!storedUser) {

            errorMessage.style.display = "block";

            errorMessage.innerHTML =
                "No account found. Please register first.";

            return;
        }


        // Convert stored data into object

        const user =
            JSON.parse(storedUser);


        // Check email

        if (email !== user.email) {

            errorMessage.style.display = "block";

            errorMessage.innerHTML =
                "Invalid email address.";

            return;
        }


        // Check password

        if (password !== user.password) {

            errorMessage.style.display = "block";

            errorMessage.innerHTML =
                "Incorrect password. Please try again.";

            return;
        }


        // Login successful

        errorMessage.style.display = "none";


        // Save login status

        localStorage.setItem(
            "womenWellAILoggedIn",
            "true"
        );


        // Go to dashboard

        window.location.href =
            "dashboard.html";

    });