<template>
  <h1 class="text-center p-4 mr-2">Generator Cerpen</h1>
    <!-- <div class="container-fluid">
      <div class="row d-flex justify-content-center">
        <div class="rounded shadow p-4 mr-2 col-6" style="width=30vw height=45vh;">
          <h2>Input Text</h2>
          <textarea v-model="inputText" placeholder="Masukkan Teks"></textarea>
          <button @click="generateText">Generate</button>
        </div> 
  
        <div class="rounded shadow p-4 mr-2 w-30 col-6" style="width=30vw height=45vh;">
          <h2>Output Text</h2>
          <textarea v-model="outputText" disabled>{{ processedText }}</textarea>
          <button @click="copyToClipboard">Copy</button>
        </div>
      </div>
    </div> -->
    <div class="px-5 rounded bg-white shadow">
      <div class="p-3">
        <div class="form-group">
          <label for="exampleInputEmail1">Input Judul</label>
          <input type="text" v-model="inputText" class="form-control" placeholder="Masukkan Judul">
        </div>
        <div class="form-group py-2">
          <button @click="loadData" class="btn btn-primary" :disabled="loading">Generate</button>
        </div>
        <div class="form-group position-relative">
          <div v-if="loading" class="position-absolute top-0 start-0 bg-secondary w-100 h-100 opacity-75 d-flex justify-content-center align-items-center">
            <div>
              <div class="spinner-border text-primary"></div>
              <div>Loading...</div>
            </div>
          </div>
          <textarea class="form-control" v-model="outputText" disabled placeholder="Hasil"></textarea>
        </div>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputText: '',
      outputText: '',
      loading: false
    };
  },
  methods: {
    loadData() {
      console.log(this.inputText );
      // Assuming you want to send the inputText as data
      // url seach param
      this.loading = true
      axios.post('http://127.0.0.1:5000/generate-story', { inputText: this.inputText }, {
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then((res) => {
          console.log(this.inputText );
          this.outputText = res.data.story;
          this.loading = false
        })
        .catch((error) => {
          console.error('Error:', error);
          this.loading = false
        });
    },
  },
};
</script>

  
  <style scoped>
  .container {
    display: flex;
    justify-content: center;
    max-width: 100%;
    margin: 0 auto;
  }
  
  
  textarea {
    width: 100%;
    height: 150px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  h1 {
    color: #006400; 
    font-size: 48px;
  }
  
  h2 {
    color: #333;
    font-size: 18px;
  }
  
  p {
    color: #666;
  }
  </style>