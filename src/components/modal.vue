<template>
    <div class="modal-overlay" @click.self="close">
      <div class="modal-container">
        <div class="modal-header">
          <h3>{{ title }}</h3>
          <button class="modal-close-button" @click="close">×</button>
        </div>
        <div class="modal-body">
          <slot></slot>
        </div>
        <div class="modal-footer">
          <button class="modal-action-button" @click="submit">{{ actionText }}</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Modal',
    props: {
      title: {
        type: String,
        default: 'Modal Title'
      },
      actionText: {
        type: String,
        default: 'Submit'
      }
    },
    methods: {
      close() {
        this.$emit('close');
      },
      submit() {
        this.$emit('submit');
      }
    }
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }
  
  .modal-container {
    background: white;
    border-radius: 8px;
    width: 400px;
    max-width: 90%;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    color: #2176FF ;
  }

  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .modal-close-button {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
  }
  
  .modal-close-button:hover {
    color: #FFA93E;
    transform: scale(1.2);
    transition: color 0.3s ease, transform 0.3s ease;
  }

  .modal-body {
    margin-top: 10px;
  }
  
  .modal-footer {
    margin-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
  
  .modal-action-button {
    background-color: #2176FF;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }
  
  .modal-action-button:hover {
    background-color: #FFA93E;
  }
  </style>
  