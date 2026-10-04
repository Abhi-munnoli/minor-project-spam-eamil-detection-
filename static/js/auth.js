/* ============================================================
   SPAMSHIELD AI - FIREBASE AUTHENTICATION
   ============================================================ */

(function () {

    "use strict";

    console.log("========================================");
    console.log("SpamShield AI Authentication Loaded");
    console.log("========================================");


    // =========================================================
    // FIREBASE CONFIGURATION
    // =========================================================

    const firebaseConfig =
        window.SPAMSHIELD_FIREBASE || null;


    if (!firebaseConfig) {

        console.error(
            "Firebase configuration was not provided by Flask."
        );

        showMessage(
            "Firebase configuration is missing.",
            "error"
        );

        return;
    }


    console.log(
        "Firebase Project:",
        firebaseConfig.projectId
    );


    // Check required configuration
    const requiredKeys = [
        "apiKey",
        "authDomain",
        "projectId",
        "appId"
    ];

    const missingKeys =
        requiredKeys.filter(
            key => !firebaseConfig[key]
        );


    if (missingKeys.length > 0) {

        console.error(
            "Missing Firebase configuration:",
            missingKeys
        );

        showMessage(
            "Firebase configuration is incomplete.",
            "error"
        );

        return;
    }


    // =========================================================
    // INITIALIZE FIREBASE
    // =========================================================

    try {

        if (!firebase.apps.length) {

            firebase.initializeApp(
                firebaseConfig
            );
        }

        console.log(
            "Firebase initialized successfully."
        );

    } catch (error) {

        console.error(
            "Firebase initialization error:",
            error
        );

        showMessage(
            "Unable to initialize Firebase.",
            "error"
        );

        return;
    }


    const auth = firebase.auth();


    // =========================================================
    // DOM ELEMENTS
    // =========================================================

    const loginForm =
        document.getElementById(
            "loginForm"
        );

    const registerForm =
        document.getElementById(
            "registerForm"
        );

    const messageBox =
        document.getElementById(
            "authMessage"
        );


    // =========================================================
    // MESSAGE FUNCTION
    // =========================================================

    function showMessage(
        message,
        type = "info"
    ) {

        const box =
            document.getElementById(
                "authMessage"
            );

        if (!box) {

            console.log(
                `[${type}] ${message}`
            );

            return;
        }

        box.textContent =
            message;

        box.className =
            `auth-message ${type}`;

        box.style.display =
            "block";
    }


    // =========================================================
    // BUTTON LOADING
    // =========================================================

    function setLoading(
        form,
        loading,
        text
    ) {

        if (!form) {
            return;
        }

        const button =
            form.querySelector(
                "button[type='submit']"
            );

        if (!button) {
            return;
        }

        if (loading) {

            button.disabled = true;

            button.dataset.originalText =
                button.textContent;

            button.textContent =
                text;

        } else {

            button.disabled = false;

            button.textContent =
                button.dataset.originalText
                || "Continue";
        }
    }


    // =========================================================
    // SEND FIREBASE TOKEN TO FLASK
    // =========================================================

    async function createFlaskSession(
        firebaseUser
    ) {

        console.log(
            "Creating Flask session..."
        );

        if (!firebaseUser) {

            throw new Error(
                "Firebase user is not available."
            );
        }


        // Get fresh Firebase ID token
        const idToken =
            await firebaseUser.getIdToken(
                true
            );


        if (!idToken) {

            throw new Error(
                "Firebase ID token could not be generated."
            );
        }


        console.log(
            "Firebase ID token received."
        );


        const response =
            await fetch(
                "/api/session",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json",

                        "Accept":
                            "application/json"
                    },

                    credentials:
                        "same-origin",

                    cache:
                        "no-store",

                    body:
                        JSON.stringify({
                            idToken:
                                idToken
                        })
                }
            );


        console.log(
            "Flask session response:",
            response.status
        );


        let data;

        try {

            data =
                await response.json();

        } catch (error) {

            throw new Error(
                "Server returned an invalid response."
            );
        }


        if (!response.ok || !data.success) {

            console.error(
                "Flask authentication failed:",
                data
            );

            throw new Error(
                data.error
                || "Unable to create server session."
            );
        }


        console.log(
            "Flask session created:",
            data.user
        );


        return data;
    }


    // =========================================================
    // LOGIN
    // =========================================================

    if (loginForm) {

        loginForm.addEventListener(
            "submit",
            async function (event) {

                event.preventDefault();

                showMessage(
                    "",
                    "info"
                );


                const emailInput =
                    document.getElementById(
                        "loginEmail"
                    );

                const passwordInput =
                    document.getElementById(
                        "loginPassword"
                    );


                if (
                    !emailInput ||
                    !passwordInput
                ) {

                    showMessage(
                        "Login form fields are missing.",
                        "error"
                    );

                    return;
                }


                const email =
                    emailInput.value
                        .trim()
                        .toLowerCase();

                const password =
                    passwordInput.value;


                if (!email || !password) {

                    showMessage(
                        "Please enter your email and password.",
                        "error"
                    );

                    return;
                }


                setLoading(
                    loginForm,
                    true,
                    "Signing in..."
                );


                try {

                    console.log(
                        "Signing into Firebase..."
                    );


                    const credential =
                        await auth.signInWithEmailAndPassword(
                            email,
                            password
                        );


                    console.log(
                        "Firebase login successful:",
                        credential.user.email
                    );


                    // Create Flask session
                    await createFlaskSession(
                        credential.user
                    );


                    showMessage(
                        "Login successful. Opening dashboard...",
                        "success"
                    );


                    // Small delay so session cookie is fully
                    // committed before navigation.
                    setTimeout(
                        function () {

                            window.location.replace(
                                "/dashboard"
                            );

                        },
                        250
                    );


                } catch (error) {

                    console.error(
                        "LOGIN ERROR:",
                        error
                    );


                    let message =
                        "Login failed.";


                    switch (
                        error.code
                    ) {

                        case
                            "auth/invalid-email":

                            message =
                                "Please enter a valid email address.";

                            break;


                        case
                            "auth/user-not-found":

                            message =
                                "No account exists with this email.";

                            break;


                        case
                            "auth/wrong-password":

                            message =
                                "Incorrect password.";

                            break;


                        case
                            "auth/invalid-credential":

                            message =
                                "Incorrect email or password.";

                            break;


                        case
                            "auth/too-many-requests":

                            message =
                                "Too many attempts. Please try again later.";

                            break;


                        case
                            "auth/user-disabled":

                            message =
                                "This account has been disabled.";

                            break;


                        default:

                            message =
                                error.message
                                || "Unable to login.";
                    }


                    showMessage(
                        message,
                        "error"
                    );

                    setLoading(
                        loginForm,
                        false
                    );
                }

            }
        );
    }


    // =========================================================
    // REGISTER
    // =========================================================

    if (registerForm) {

        registerForm.addEventListener(
            "submit",
            async function (event) {

                event.preventDefault();


                const nameInput =
                    document.getElementById(
                        "registerName"
                    );

                const emailInput =
                    document.getElementById(
                        "registerEmail"
                    );

                const passwordInput =
                    document.getElementById(
                        "registerPassword"
                    );

                const confirmInput =
                    document.getElementById(
                        "confirmPassword"
                    );


                if (
                    !nameInput ||
                    !emailInput ||
                    !passwordInput ||
                    !confirmInput
                ) {

                    showMessage(
                        "Registration form fields are missing.",
                        "error"
                    );

                    return;
                }


                const name =
                    nameInput.value.trim();

                const email =
                    emailInput.value
                        .trim()
                        .toLowerCase();

                const password =
                    passwordInput.value;

                const confirmPassword =
                    confirmInput.value;


                // Validation
                if (!name) {

                    showMessage(
                        "Please enter your name.",
                        "error"
                    );

                    return;
                }


                if (!email) {

                    showMessage(
                        "Please enter your email.",
                        "error"
                    );

                    return;
                }


                if (password.length < 6) {

                    showMessage(
                        "Password must contain at least 6 characters.",
                        "error"
                    );

                    return;
                }


                if (
                    password !==
                    confirmPassword
                ) {

                    showMessage(
                        "Passwords do not match.",
                        "error"
                    );

                    return;
                }


                setLoading(
                    registerForm,
                    true,
                    "Creating account..."
                );


                try {

                    console.log(
                        "Creating Firebase account..."
                    );


                    const credential =
                        await auth.createUserWithEmailAndPassword(
                            email,
                            password
                        );


                    console.log(
                        "Firebase account created."
                    );


                    const firebaseUser =
                        credential.user;


                    // Save display name
                    await firebaseUser.updateProfile({
                        displayName:
                            name
                    });


                    // Force fresh token
                    await firebaseUser.getIdToken(
                        true
                    );


                    // Create Flask session
                    await createFlaskSession(
                        firebaseUser
                    );


                    showMessage(
                        "Account created. Opening dashboard...",
                        "success"
                    );


                    setTimeout(
                        function () {

                            window.location.replace(
                                "/dashboard"
                            );

                        },
                        250
                    );


                } catch (error) {

                    console.error(
                        "REGISTER ERROR:",
                        error
                    );


                    let message =
                        "Registration failed.";


                    switch (
                        error.code
                    ) {

                        case
                            "auth/email-already-in-use":

                            message =
                                "An account already exists with this email.";

                            break;


                        case
                            "auth/invalid-email":

                            message =
                                "Please enter a valid email address.";

                            break;


                        case
                            "auth/weak-password":

                            message =
                                "Password is too weak.";

                            break;


                        case
                            "auth/operation-not-allowed":

                            message =
                                "Email/password authentication is not enabled in Firebase.";

                            break;


                        default:

                            message =
                                error.message
                                || "Unable to create account.";
                    }


                    showMessage(
                        message,
                        "error"
                    );

                    setLoading(
                        registerForm,
                        false
                    );
                }

            }
        );
    }


    // =========================================================
    // AUTH STATE MONITOR
    // =========================================================

    auth.onAuthStateChanged(
        function (user) {

            if (user) {

                console.log(
                    "Firebase user:",
                    user.email
                );

            } else {

                console.log(
                    "No Firebase user currently signed in."
                );
            }

        }
    );

})();