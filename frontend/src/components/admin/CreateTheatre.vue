<template>
  <div class="container">
    <br />
    <div class="card">
      <div class="card-header">
        <h2>Add Theatre</h2>
      </div>
      <div class="card-body">
        <div v-if="error" class="alert alert-danger">
          <strong>Error!</strong> Invalid Parameter.
        </div>
        <form @submit.prevent="handleForm">
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input
              v-model="theatre.name"
              type="text"
              class="form-control"
              id="name"
            />
          </div>
          <div class="mb-3">
            <label for="place" class="form-label">Place</label>
            <input
              v-model="theatre.place"
              type="text"
              class="form-control"
              id="place"
            />
          </div>
          <div class="mb-3">
            <label for="capacity" class="form-label">Capacity</label>
            <input
              v-model="theatre.capacity"
              type="number"
              class="form-control"
              id="capacity"
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
  name: "CreateTheatreComponent",
  data() {
    return {
      theatre: {},
      error: null,
    };
  },
  methods: {
    handleForm() {
      const API_URL = "http://localhost:5000/api/theatres/";

      axios
        .post(API_URL, {
          name: this.theatre.name,
          place: this.theatre.place,
          capacity: this.theatre.capacity,
        })
        .then(() => {
          this.$router.push("/theatres");
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>

<style></style>
