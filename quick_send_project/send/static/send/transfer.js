//Returns true if there is enough in the originator account to be sent out
balance_sufficient = (originator,amount)=>{
  return new Promise(function(resolve,reject){
    const request = new Request('/api/lookup/' + originator)
    fetch(request).then(response => response.json()).then(
      (data)=>{
        if (data['final_balance'] >= amount){
          //enough money, at least in some situations
          //transfer
          resolve(true)
        }else{
          resolve(false)
        }
      }
    )  
  })
}

document.getElementById('send').onclick = ()=>{
//  originator = 'tb1qqkz98e04vakzrprqlehqr46hmx9a98jh586al6'
//  receiver = 'tb1q5xa93se9aqag6n4wphuc9hzs7g8vre8elw04gy'
  originator = document.getElementById('originator').value
  receiver = document.getElementById('receiver').value
  amount = document.getElementById('amount').value

  balance_sufficient(originator,amount).then((result)=>{
    if (result){
      //Proceed with the transfer
      //alert('transfer proceeds')
      const request = new Request('/api/send/' + originator + ',' + receiver + ',' + amount)
      fetch('')
    }
    else{
      alert('Insufficient funds')
    }
  })
}

