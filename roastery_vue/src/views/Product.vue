<template>
    <div class="Product-page">
        <div class="columns is-multiline">
            <div class="column is-6">
                <figure class="image is-3by2">
                    <img v-bind:src="product.get_image" alt="Image">
                </figure>
            </div>

            <div class="column">
                <h2 class="title">Information</h2>

                <h5 class="subtitle is-4">{{product.name}}</h5>
                <p class="mb-5">{{product.description}}</p>

                <p><strong>Price: </strong>IDR {{ product.price }}</p>

                <div class="field has-addons mt-3">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "Product",
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted(){
        this.getProduct()
    },
    methods: {
        async getProduct(){
            const product_slug = this.$route.params.product_slug
            const category_slug = this.$route.params.category_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}/`)
                .then(response => {
                    this.product = response.data
                })
                .catch(error => {
                    console.log(error)
                })

        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity += 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
        }
    }
}
</script>

