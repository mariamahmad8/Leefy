function showEnterPlace() {
  let addInfoContainer = document.getElementById('add-the-info');
  addInfoContainer.classList.toggle('pressedAdd');
}

function addThePlant() {

  const nameInput = document.querySelector('.input-information[type="text"]:nth-child(1)');
  const locationInput = document.querySelector('.input-information[type="text"]:nth-child(2)');

  const plantName = nameInput.value;
  const plantLocation = locationInput.value;

  
  const newPlant = document.createElement('div');
  newPlant.className = 'plant';
  
  
  newPlant.innerHTML = `
    <div class="plant-image-container">
      <img class="plant-image" src="https://hgic.clemson.edu/wp-content/uploads/2004/12/chinese-hibiscus-hibiscus-rosa-sinensis-has-four.jpeg" alt="${plantName}">
    </div>
    <div class="plant-name-container">
      <div class="plant-name">${plantName}</div>
      <div class="location">${plantLocation}</div>
    </div>
  `;

  const plantContainer = document.querySelector('.my-plant-container');
  plantContainer.appendChild(newPlant);
  

  nameInput.value = '';
  locationInput.value = '';
}


document.getElementById('submit-plant-button').addEventListener('click', function() {
  addThePlant(); 
});