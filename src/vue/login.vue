<template>
    <div class="login_page">
    <div class="photo">
      <img  class="bateau" src="../../public/login.png">
    </div>
    <div2 class="infodiv">
        <logo/>
      <p class="input"> login </p>
      <input class="login" type="text" placeholder="email">
      <p class="input"> password </p>
      <input class="password" type="password" placeholder="password">
        <button class="forgot"> Forgot password?</button>
        <p class="remember">
            <img class="btrm" src="../../public/bg-switcher.svg" @click="rememberMe = !rememberMe" :class="{ active: rememberMe }">
            <p> Remember me</p>
        </p>
      <button class="signin"> Sign in</button>
      <button class="google"> <img src="../../public/icon-google.png"> <p> Sign in with Google</p> </button>
      <button class="apple"> <img src="../../public/icon-apple.svg"> <p> Sign in with Apple</p> </button>
      <p class="DOESNT"> Don't have an account? <button class="signup" href="#"> Sign up now</button></p>
    </div2>
</div>
  </template>

<script>
  import Poppins from '../../public/Poppins-Regular.ttf'
  import logo from '../components/logo.vue'

  export default {
    name: 'Login',
    components: {
      logo
    },
    data() {
    return {
      rememberMe: false,
    };
  },
  }
</script>

  <style>

.forgot {
    color: #FCD19C;
    font-family: Poppins;
    font-size: 12px;
    font-style: normal;
    font-weight: 400;
    line-height: 12px;
    letter-spacing: 0.3px;
}

input {
  font-size: 20px;
}

.remember {
    display: flex;
    height: 45.5px;
    align-items: center;
    gap: 25.025px;
    border-radius: 2.275px;
    font-size: 100%;
    background: #FFF;
  }

  .apple {
    display: flex;
    height: 48px;
    width: fit-content;
    padding: 12px 15px;
    font-size: 100%;
    justify-content: center;
    align-items: center;
    gap: 15px;
    border-radius: 8px;
    border: 1px solid #000;
    background: #FFF;
    box-shadow: 3px 3.1375px 2.275px 3px rgba(0, 0, 0, 0.25), 0px 0px 0px 0px rgba(0, 0, 0, 0.08);
  }

  .google {
    display: flex;
    font-size: 100%;
    height: 50.5px;
    width: fit-content;
    padding: 0px 13.65px;
    align-items: center;
    gap: 25.025px;
    border-radius: 5px;
    background: #FFF;
    box-shadow: 3px 3.1375px 2.275px 3px rgba(0, 0, 0, 0.25), 0px 0px 0px 0px rgba(0, 0, 0, 0.08);
  }

.infodiv {
  display: flex;
  width: 40%;
  padding: 43px 64px 102.82px 63px;
  flex-direction: column;
  align-items: center;
  align-self: stretch;
  gap : 5%;
}

.bateau {
  height: 100%;
  width: 100%;
  object-fit: cover;

}

@media only screen and (max-width: 768px) {
  .photo {
    display: none;
  }
  .infodiv {
    width: auto;
  }
  p {
    font-size: 16px;
  }
  .google p,
  .apple p {
    display: none;
  }
  .google{
    width: auto;
    border-radius: 5px;
  }
  .infodiv {
    gap: 25px;
  }
  input {
    height: 40px;
  }
  .password {
    width: 100%;
  }
  .login {
    width: 100%;
  }
  .remember {
    width: 100%;
  }
}

.photo {
  width: 75%;
  height: 100vh;
}

.titre {
    display: flex;
    padding-left: 63px;
    flex-direction:row;
    align-items: center;
    align-self: stretch;
}

.input {
    display: flex;
    color: var(--black-800333333, #333);
    font-family: Poppins;
    font-size: 15px;
    font-weight: 400;
    line-height: 12px;
    letter-spacing: 0.3px;
    align-items:flex-start;
}

.signin {
    color: var(--white-ffffff, #FFF);
    display: flex;
    width : 60%;
    padding: 10px 24px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 100%;
    background: var(--system-blue-007-aff, #007AFF);
    border-radius: 10px;
    box-shadow: 1.5px 2.1375px 1.275px 1px rgba(0, 0, 0, 0.25), 0px 0px 0px 0px rgba(0, 0, 0, 0.08);
}

.signin:hover {
    background: #2176FF;
}

.login_page {
    display: flex;
    flex-direction: row;
  }

  .DOESNT {
    display: flex;
    color: var(--black-800333333, #333);
    font-family: Poppins;
    font-size: 15px;
    font-weight: 400;
    line-height: 12px;
    letter-spacing: 0.3px;
  }

  .signup {
    color: var(--system-blue-007-aff, #007AFF);
    font-family: Poppins;
    font-size: 15px;
    font-weight: 400;
    line-height: 12px;
    letter-spacing: 0.3px;
    justify-content: center;
  }

  .login {
    display: flex;
    border: 1px solid #000;
    border-radius: 8px;
    align-content: center;
    text-align: center;
    padding-top: 2px;
   }

   .password {
    display: flex;
    border: 1px solid #000;
    border-radius: 8px;
    align-content: center;
    text-align: center;
    padding-top: 2px;
    text-overflow: clip;
   }

   .apple p,
   .google p{
    text-wrap: none;
   }

   .remember.btrm.active {
    src: url('../../public/bg-switcher.svg');
   }

</style>