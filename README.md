# 21 Coding Challenge - Backend (FastAPI)

## The case study: Application review

Reviewing applications is one of the key activities when starting a new project.
To tackle that challenge, BP ACCELERATOR Inc. wants to provide an API, via which applicants can hand in their application with past project experience.

The software stores the data in a database and generates a document so the application can be reviewed by the HR department.

## Product Requirements

As an applicant at BP ACCELERATOR Inc.,

- [ ] I want to provide my application via a REST-API, with the following data:
  - [ ] my work e-mail address
  - [ ] a name
  - [ ] a github user
  - [ ] past projects (min 1)
- [ ] for each past project I want to provide:
  - [ ] name of the project
  - [ ] employment mode (options: freelance / employed)
  - [ ] capacity (options: part-time / full-time)
  - [ ] duration in months (allow to provide weeks)
  - [ ] start year
  - [ ] role
  - [ ] team size (number)
  - [ ] link to the repository (optional)
  - [ ] link to the live url (optional)

As an application reviewer at BP ACCELERATOR Inc.,

- [ ] I want to see an overview of all applications in the database
- [ ] I want that when new data for an e-mail address is provided, all old data is automatically deleted
- [ ] I want to easily generate and download a PDF document that lists the data provided by the applicant
  - [ ] the PDF contains the GitHub profile image of the applicant ([API](https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api))

## Your Mission

Create a **FastAPI** application that satisfies all must-have requirements above, plus any nice-to-have requirements you wish to include.

For that, you'll need to provide a REST-API, set up a database, and generate a PDF document that contains the applicant's data.

**Technical Constraints:**
* You must use **FastAPI**.
* You must use **Alembic** for database migrations.
* The final delivery must be running with **Docker**.

You can use any boilerplate/approach you prefer, but try to keep it simple. We encourage you to use your favorite tools and packages to build a solid FastAPI application.

You don't have to host your service publicly, but feel free to do that.
Please include a description in the README.md how to run the project locally and provide us a well-done description for the API.

## Instructions

- Fork this repo.
- The challenge is on!
- Build a performant, clean, and well-structured solution.
- Commit early and often. We want to be able to check your progress.
- Please complete your working solution within 2 days of receiving this challenge.
- Additionally to the solution, please hand in the PDF document, filled with your actual project experience.

### Submission & Walkthrough

Once you are ready for review, please notify us with a link to your repo. **You must also include a Loom video (or similar screen recording) containing the following:**

1.  **Solution Walkthrough:** Briefly show your solution working and explain how you got there.
2.  **AI Usage & Reasoning:** We encourage the use of AI tools (ChatGPT, Claude, Copilot, etc.).
    * If you used AI, you **must** provide reasoning for why you chose that specific model or tool.
    * You must show your prompts and the chat conversation history in the video to demonstrate how you worked with the AI to reach your solution.
    * If you did *not* use AI, please explain your reasoning for working without it.

**Happy coding!**

## License

We have licensed this project under the MIT license so that you may use this for a portfolio piece (or anything else!).
