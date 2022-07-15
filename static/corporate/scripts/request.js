let totalPrice = 0;
let totalItems = 0;

document.getElementById("add-button").addEventListener("click", async (e) => {
  e.preventDefault();

  try {
    const response = await fetch('{% url "cart:add to cart" %}', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        productid: document.getElementById("add-button").value,
        productqty: document.getElementById("product-quantity").value,
        productprice: document.querySelector("div.price").title,
        csrfmiddlewaretoken: "{{csrf_token}}",
      }),
    });

    if (response.ok != false) {
      const error = await response.json();
      throw new Error(error.message);
    }
    const data = response.json();
    console.log(data)

    // totalPrice += Number(json.price) * Number(json.qty);
    // totalItems += Number(json.qty);
    // json.qty = totalItems;
    // json.price = totalPrice;
    // // document.querySelector(".top-cart-info-value").innerText = `${totalPrice.toFixed(2)}`
    // document.querySelector(".top-cart-info-count").innerText = json.qty;
  } catch (error) {
    console.error(error.message);
  }
});
