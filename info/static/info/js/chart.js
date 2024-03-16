// ASSEMBLY STANDARD
const totalCollectedElement = document.querySelector('.chart_collected p'),
      currentQuantity = document.querySelector('.chart_collected'),
      assemblingElement = document.querySelector('.task_assembling'),
      result = document.querySelector('.chart_collected p')

let totalCollected = parseInt(totalCollectedElement.textContent),
    assembling = parseInt(assemblingElement.textContent);

function updateChart(total, assembling) {
    totalCollected = total;

    const percentage = (totalCollected / assembling) * 100,
          height = (percentage / 100) * 300;

    currentQuantity.style.height = height + 'px';

    if (percentage >= 50 && percentage < 70) {
        currentQuantity.style.backgroundColor = '#FFD700';
    } else if (percentage >= 70) {
        currentQuantity.style.backgroundColor = '#00FF00';
    } else {
        currentQuantity.style.backgroundColor = '#8B0000';
    }
    result.textContent = `${totalCollected} кор. ${percentage.toFixed(0)}%`;
}

const newTotalCollected = parseInt(totalCollectedElement.textContent);
totalCollectedElement.textContent = newTotalCollected;

updateChart(newTotalCollected, assembling);


// TRANSPORTED STANDARD
const totalTransportedElement = document.querySelector('.chart_transported p'),
      currentQuantityTransported = document.querySelector('.chart_transported'),
      transportedElement = document.querySelector('.task_transported_pallet'),
      resultTransported = document.querySelector('.chart_transported p');

let totalTransported = parseInt(totalTransportedElement.textContent),
    transported = parseInt(transportedElement.textContent);
    
function updateTransported(totalTr, transported) {
    totalTransported = totalTr;

    const percTransported = (totalTransported / transported) * 100,
          heightTr = (percTransported / 100) * 300;
    
    currentQuantityTransported.style.height = heightTr + 'px';    
    
    if (percTransported >= 50 && percTransported < 70) {
        currentQuantityTransported.style.backgroundColor = '#FFD700';
    } else if (percTransported >= 70) {
        currentQuantityTransported.style.backgroundColor = '#00FF00';
    } else {
        currentQuantityTransported.style.backgroundColor = '#8B0000';
    }
    resultTransported.textContent = `${totalTransported} пал. ${percTransported.toFixed(0)}%`;
}

const newTotalTransported = parseInt(totalTransportedElement.textContent);
totalTransportedElement.textContent = newTotalTransported;

updateTransported(newTotalTransported, transported)



// COMING_CAR STANDARD
const totalComingCarElement = document.querySelector('.chart_discharge p'),
      currentQuantityComingCar = document.querySelector('.chart_discharge'),
      comingCarElement = document.querySelector('.task_coming_car'),
      resultComingCar = document.querySelector('.chart_discharge p');

let totalComingCar = parseInt(totalComingCarElement.textContent),
    comingCar = parseInt(comingCarElement.textContent);      

function updateComingCar(totalCar, comingCar) {
    totalComingCar = totalCar;

    const percComingCar = (totalComingCar / comingCar) * 100,
          heightC = (percComingCar / 100) * 300;
    
    currentQuantityComingCar.style.height = heightC + 'px';   

    if (percComingCar >= 50 && percComingCar < 70) {
        currentQuantityComingCar.style.backgroundColor = '#FFD700';
    } else if (percComingCar >= 70) {
        currentQuantityComingCar.style.backgroundColor = '#00FF00';
    } else {
        currentQuantityComingCar.style.backgroundColor = '#8B0000';
    }
    resultComingCar.textContent = `${totalComingCar} маш. ${percComingCar.toFixed(0)}%`;
}

const newTotalComingCar = parseInt(totalComingCarElement.textContent);
totalComingCarElement.textContent = newTotalComingCar;

updateComingCar(newTotalComingCar, comingCar)


// OUT_CAR STANDARD
const totalOutCarElement = document.querySelector('.chart_shipment p'),
      currentQuantityOutCar = document.querySelector('.chart_shipment'),
      outCarElement = document.querySelector('.task_out_car'),
      resultOutCar = document.querySelector('.chart_shipment p');

let totalOutCar = parseInt(totalOutCarElement.textContent),
    outCar = parseInt(outCarElement.textContent);        

function updateOutCar(totalOut, outCar) {
    totalOutCar = totalOut;
    
    const percOutCar = (totalOutCar / outCar) * 100,
    heightO = (percOutCar / 100) * 300;

    currentQuantityOutCar.style.height = heightO + 'px';

    if (percOutCar >= 50 && percOutCar < 70) {
        currentQuantityOutCar.style.backgroundColor = '#FFD700';
    } else if (percOutCar >= 70) {
        currentQuantityOutCar.style.backgroundColor = '#00FF00';
    } else {
        currentQuantityOutCar.style.backgroundColor = '#8B0000';
    }
    resultOutCar.textContent = `${totalOutCar} маш. ${percOutCar.toFixed(0)}%`;
}

const newTotalOutCar = parseInt(totalOutCarElement.textContent);
totalOutCarElement.textContent = newTotalOutCar;

updateOutCar(newTotalOutCar, outCar)

// OTHER STANDARD
const totalOtherElement = document.querySelector('.chart_others p'),
      currentQuantityOther = document.querySelector('.chart_others'),
      otherElement = document.querySelector('.task_other'),
      resultOther = document.querySelector('.chart_others p');

let totalOther = parseInt(totalOtherElement.textContent),
    other = parseInt(otherElement.textContent);        

    function updateOther(totalOth, other) {
        totalOther = totalOth;
        
        const percOther = (totalOther / other) * 100,
        heightOther = (percOther / 100) * 300;
    
        currentQuantityOther.style.height = heightOther + 'px';      
    
        if (percOther <= 100) {
            currentQuantityOther.style.backgroundColor = '#00FF00';
        } else if (percOther >= 101 && percOther <= 110) {
            currentQuantityOther.style.backgroundColor = '#FFD700';
        } else if (percOther >= 120) {
            currentQuantityOther.style.backgroundColor = '#8B0000';
        }
        resultOther.textContent = `Время ${totalOther} ч. ${percOther.toFixed(0)}%`;    
}

const newTotalOther = parseInt(totalOtherElement.textContent);
totalOtherElement.textContent = newTotalOther;

updateOther(newTotalOther, other)