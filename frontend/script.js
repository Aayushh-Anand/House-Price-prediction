const form = document.getElementById("predictionForm");
const button = document.getElementById("predictBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const errorBox = document.getElementById("error");
const priceElement = document.getElementById("predictedPrice");


form.addEventListener("submit", async (event) => {

    event.preventDefault();

    result.classList.add("hidden");
    errorBox.classList.add("hidden");

    button.disabled = true;
    loading.classList.remove("hidden");

    const data = {
        Area: Number(document.getElementById("Area").value),
        BHK: Number(document.getElementById("BHK").value),
        Bathroom: Number(document.getElementById("Bathroom").value),

        Furnishing:
            document.getElementById("Furnishing").value,

        Locality:
            document.getElementById("Locality").value,

        Parking:
            document.getElementById("Parking").value,

        Status:
            document.getElementById("Status").value,

        Transaction:
            document.getElementById("Transaction").value,

        Type:
            document.getElementById("Type").value
    };


    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });


        const resultData = await response.json();


        if (!response.ok) {
            throw new Error(
                resultData.detail ||
                "Prediction failed"
            );
        }


        const price =
            Number(resultData.predicted_price);


        priceElement.textContent =
            "₹" +
            price.toLocaleString("en-IN", {
                maximumFractionDigits: 0
            });


        result.classList.remove("hidden");

    } catch (error) {

        errorBox.textContent =
            error.message;

        errorBox.classList.remove("hidden");

    } finally {

        loading.classList.add("hidden");
        button.disabled = false;
    }

});