<template>
  <div class="container">
    <br />
    <div class="card">
      <div class="card-header">
        <h2>Edit Show</h2>
      </div>
      <div class="card-body">
        <div v-if="error" class="alert alert-danger">
          <strong>Error!</strong> Invalid Parameter.
        </div>
        <form @submit.prevent="handleForm">
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input
              v-model="show.name"
              type="text"
              class="form-control"
              id="name"
            />
          </div>
          <div class="mb-3">
            <label for="rate" class="form-label">Rate</label>
            <input
              v-model="show.rate"
              type="number"
              step="0.1"
              class="form-control"
              id="rate"
            />
          </div>
          <div class="mb-3">
            <label for="tags" class="form-label">Tags</label>
            <input
              v-model="show.tags"
              type="text"
              class="form-control"
              id="tags"
            />
          </div>
          <div class="mb-3">
            <label for="price" class="form-label">Price</label>
            <input
              v-model="show.price"
              type="number"
              step="0.01"
              class="form-control"
              id="price"
            />
          </div>
          <div class="d-flex flex-row-reverse">
            <router-link to="/theatres" class="btn btn-primary">
              Back
            </router-link>
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../../services/axios-config";

export default {
  name: "EditShowComponent",
  data() {
    return {
      show: {},
      error: null,
    };
  },
  created() {
    const API_URL = `http://localhost:5000/api/shows/${this.$route.params.id}`;

    axios
      .get(API_URL)
      .then((response) => {
        this.show.id = response.data.id;
        this.show.name = response.data.name;
        this.show.rate = response.data.rate;
        this.show.tags = response.data.tags;
        this.show.price = response.data.price;
        this.show.theatre_id = response.data.theatre_id;
      })
      .catch(() => {});
  },
  methods: {
    handleForm() {
      const API_URL = `http://localhost:5000/api/shows/${this.$route.params.id}`;

      axios
        .put(API_URL, {
          name: this.show.name,
          rate: this.show.rate,
          tags: this.show.tags,
          price: this.show.price,
          theatre_id: this.show.theatre_id,
        })
        .then(() => {
          this.$router.push(`/theatres/${this.show.theatre_id}/shows`);
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>

<style></style>
