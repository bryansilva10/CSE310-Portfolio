<template>
  <div id="app">
    <h1 class="subtitle has-text-centered">Bucket List:</h1>
    <hr />
    <div class="field has-addons">
      <div class="control is-expanded">
        <input
          class="input"
          v-model="description"
          type="text"
          placeholder="Go to mars..."
        />
      </div>
      <div class="control">
        <a class="button is-info" @click="addItem" :disabled="!description"
          >Add</a
        >
      </div>
    </div>
    <div class="notification" v-for="(item, i) in items" :key="item._id">
      <div class="columns">
        <input
          class="column input"
          v-if="isSelected(item)"
          v-model="editedDescription"
        />
        <p v-else class="column">
          <span class="tag is-primary">{{ i + 1 }}</span>
          {{ item.description }}
        </p>
        <div class="column is-narrow">
          <span
            class="icon has-text-primary"
            @click="isSelected(item) ? unselect() : select(item)"
          >
            <i class="material-icons">{{
              isSelected(item) ? "close" : "edit"
            }}</i>
          </span>

          <span
            class="icon has-text-info"
            @click="
              isSelected(item) ? updateItem(item, i) : removeItem(item, i)
            "
          >
            <i class="material-icons">{{
              isSelected(item) ? "save" : "delete"
            }}</i>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import axios
import axios from "axios";

//export vue app
export default {
  name: "App",

  //data for app
  data() {
    return {
      //store items and their features
      items: [],
      description: "",
      editedDescription: "",
      selected: {},
    };
  },

  //hook to perform ajax call when DOM is being rendered
  async mounted() {
    //await axios
    const response = await axios.get("api/items/");
    //store data in the items array (state)
    this.items = response.data;
  },

  //methods for app
  methods: {
    //Create item
    async addItem() {
      //post to api with description
      const response = await axios.post("api/items/", {
        description: this.description,
      });

      //push to array of items
      this.items.push(response.data);

      //reset description on form input to be blank
      this.description = "";
    },

    //remove item
    async removeItem(item, i) {
      //make request with id as param
      await axios.delete("api/items/" + item._id);

      //remove item from array and DOM
      this.items.splice(i, 1);
    },

    //select an item
    select(item) {
      //set selected objec with values from item
      this.selected = item;

      //set the description to be updated
      this.editedDescription = item.description;
    },

    //define if item is selected
    isSelected(item) {
      return item._id === this.selected._id;
    },

    //unselect an item
    unselect() {
      //empty out the selected object
      this.selected = {};

      //set edited to empty string
      this.editedDescription = "";
    },

    //update an item
    async updateItem(item, i) {
      //make request
      const response = await axios.put("api/items/" + item._id, {
        //data to update
        description: this.editedDescription,
      });

      //update item in array with response
      this.items[i] = response.data;
      //unselect to leave edit mode
      this.unselect();
    },
  },
};
</script>

<style>
#app {
  margin: auto;
  margin-top: 3rem;
  max-width: 700px;
}
.icon {
  cursor: pointer;
}
</style>
