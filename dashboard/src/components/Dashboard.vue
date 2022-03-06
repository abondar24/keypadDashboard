<template>
  <div class="container-fluid">
     <div class="row">
        <h1>Keypad Dashboard</h1>
     </div>
     <div class="row" style="margin-top:10px;">
       <div class="col col-sm">
       </div>
       <div class="col col-sm">
         <button id="connect" class="btn btn-dark" v-on:click="handleConnect">Connect to queue</button>
         <button id="connect" class="btn btn-danger" v-on:click="handleDisconnect">Disconnect from queue</button>
       </div>
       <div class="col col-sm">
       </div>
     </div>
     <div class="row" style="margin-top:10px;">

       <div v-for="item in incoming" :key="item">
          <p>Incoming key:{{item.msg}}</p>
    </div>
     </div>
  </div>
</template>

<script>
import Stomp from "webstomp-client";
export default {
  name: 'Dashboard',
  data() {
    return {
      incoming: [],
      client: null,
      socket: null,
      stompEndpoint: 'ws://localhost:61613'
    }
  },
  methods: {
    handleConnect(){
      this.client = Stomp.client(this.stompEndpoint);
      var headers = {
        login: 'admin',
        passcode: 'keypadAdmin'
      }

      this.client.connect(headers,
         frame =>{
             console.log(frame)
             this.client.subscribe("keypad",tick=>{
               var body = JSON.parse(tick.body)
               console.log(body)
               this.incoming.push(JSON.parse(tick.body))
             })
         //
       },
       error => {
                 console.log(error)
               }
     )
    },
    handleDisconnect(){
      if (this.client) {
        this.client.disconnect();
      }
    }
  }

}
</script>
