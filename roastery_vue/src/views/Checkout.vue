<template>
    <div class="checkout-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-7 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>

                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zip code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="field">
                    <label>Place*</label>
                    <div class="control">
                        <input type="text" class="input textarea" v-model="place">
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Submit Payment</button>
                </template>
            </div>

            <div class="column is-5">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>IDR {{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>IDR {{ getItemTotal(item) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>IDR {{ cartTotalPrice}}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            first_name:'',
            last_name:'',
            email:'',
            phone:'',
            address:'',
            zipcode:'',
            place:'',
            errors:[],
        }
    },
    mounted() {
        document.title = 'Checkout | Rana'
        
        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        async submitForm(){
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('The first name should not be empty!')
            }
            if (this.last_name === '') {
                this.errors.push('The last name should not be empty!')
            }
            if (this.email === '') {
                this.errors.push('The email should not be empty!')
            }
            if (this.phone === '') {
                this.errors.push('The phone should not be empty!')
            }
            if (this.address === '') {
                this.errors.push('The address should not be empty!')
            }
            if (this.zipcode === '') {
                this.errors.push('The zip code should not be empty!')
            }
            if (this.place === '') {
                this.errors.push('The place should not be empty!')
            }
            if (!this.errors.length) {
                const items = []
                for (let i = 0; i < this.cart.items.length; i++) {
                    const item = this.cart.items[i]
                    const obj = {
                        product: item.product.id,
                        quantity: item.quantity,
                        price: item.product.price * item.quantity
                    }
                    items.push(obj)
                }
                const data = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'address': this.address,
                    'zipcode': this.zipcode,
                    'place': this.place,
                    'phone': this.phone,
                    'items': items,
                }

                await axios
                    .post('/api/v1/checkout/', data, {headers: {"Authorization": "Token " + this.$store.state.token }})
                    .then(response => { 
                        this.$store.commit('clearCart')
                        this.$router.push('/cart/success')
                    })
                    .catch(error => {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(error)
                    })
            }
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>