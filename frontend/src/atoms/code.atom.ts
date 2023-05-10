import { atom } from "recoil";

export const problemOpenState = atom({
  key: "problemOpenState",
  default: {},
});

export const nowProblemSubmissionIdState = atom({
  key: "nowProblemSubmissionIdState",
  default: {
    problemTitle: "",
    problemId: 0,
    problemLevel: 0,
    submissionId: 0,
  },
});
