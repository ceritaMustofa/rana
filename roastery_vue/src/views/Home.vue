<template>
  <div class="home">
    <section class="hero banner is-primary mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Rana Roastery
        </p>
        <p class="subtitle">
          We serve the best Roasted Coffee bean in Town
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted()  {
    this.getLatestProducts()

    document.title = 'Rana Roastery'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
          console.log(response)
        })

        .catch(error => {
          console.log(error)
        })

        this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.banner {
  height: 75vh;
  background-image: url(../assets/coffee.jpg);
  background-repeat: no-repeat;
  background-size: 100%;
}
.hero-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
