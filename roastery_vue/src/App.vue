<template>
  <div id="wrapper">
    <nav class="navbar">
      <div class="navbar-brand ml-4">
        <router-link to="/" class="navbar-item">
          <img src="./assets/rana.png" alt="">
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      
      

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <router-link class="navbar-item" to="/">RANA ROASTERY</router-link>
          <router-link class="navbar-item" to="/about">ABOUT</router-link>

          <div class="navbar-item">
            <form action="/search" method="get">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input is-dark is-outlined" placeholder="Search your items here" name="query">
                </div>
                <div class="control">
                  <button class="button is-dark is-outlined">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/house-blend" class="navbar-item">HOUSE BLEND</router-link>
          <router-link to="/single-origin" class="navbar-item">SINGLE ORIGIN</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-dark is-outlined">Account</router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-dark is-outlined">Log In</router-link>
              </template>

              <router-link to="/cart" class="button is-dark is-outlined">
                  <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                  <span>Cart ({{ cartTotalLength }})</span>
              </router-link>

            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view/>
    </section>

    <footer class="hero-foot">
      <div class="content has-text-centered">
        <p>
          <span> Copyright  (c) 2021</span>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Bearer" + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';

:root {
      --brandColor: hsl(166, 67%, 51%);
      --background: rgb(255, 255, 255);
      --textDark: hsla(0, 0%, 0%, 0.66);
      --textLight: hsla(0, 0%, 0%, 0.33);
    }
.field:not(:last-child) {
    margin-bottom: 1rem;
  }

  .register {
    margin-top: 1rem;
    background: rgb(208, 205, 205);
    border-radius: 10px;
  }

  .left,
  .right {
    padding: 3rem;
  }

  .left {
    border-right: 5px solid var(--background);
  }

  .left .title {
    font-weight: 800;
    letter-spacing: -2px;
  }

  .left .colored {
    color: var(--brandColor);
    font-weight: 500;
    margin-top: 1rem !important;
    letter-spacing: -1px;
  }

  .left p {
    color: var(--textLight);
    font-size: 1.15rem;
  }

  .right .title {
    font-weight: 800;
    letter-spacing: -1px;
  }

  .right .description {
    margin-top: 1rem;
    margin-bottom: 1rem !important;
    color: var(--textLight);
    font-size: 1.15rem;
  }

  .right small {
    color: var(--textLight);
  }

  input {
    font-size: 1rem;
  }

  input:focus {
    border-color: var(--brandColor) !important;
    box-shadow: 0 0 0 1px var(--brandColor) !important;
  }

  .fab,
  .fas {
    color: var(--textLight);
  }
    
</style>
