<template>
     <tr>
         <td ><router-link :to="item.product.get_absolute_url" class="has-text-dark ">{{ item.product.name }}</router-link></td>
         <td>IDR {{ item.product.price.toLocaleString() }}</td>
         <td>
             {{ item.quantity }}
             <a class="has-text-grey is-size-4" @click="decrementQuantity(item)">-</a>
             <a class="has-text-grey is-size-5" @click="incrementQuantity(item)">+</a>
         </td>
         <td>IDR {{ getItemTotal(item).toLocaleString() }}</td>
         <td><button class="delete" @click="removeFromCart(item)"></button></td>
     </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1
            
            if(item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
            
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1
            
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        }
    }
}
</script>