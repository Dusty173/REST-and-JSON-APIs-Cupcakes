const BASE_URL = 'http://localhost:5000/api';

function generateCupcakeHTML(cupcake){
    return `<div data-cupcake-id=${cupcake.id}
        <li> ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
        </li>
        <img class=Cupcake-img src="${cupcake.image}"
        </div>`;
}

async function getCupcakesList(){
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for(let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcakeData));
        $("#all_cupcakes").append(newCupcake);
    }
}

$("#add-cupcake-form").on("submit", async function(e){
    e.preventDefault();
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCupcakeRespone =  await axios.post(`${BASE_URL}/cupcakes`, {flavor, rating, size, image});
    
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});

$("#all_cupcakes").on("click", ".delete-button", async function(e){
    e.preventDefault();
    let $cupcake = $(e.target).closest('div');
    let cupcakeId = $cupcake.attr('data-cupcake-id');

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
});

$(getCupcakesList);