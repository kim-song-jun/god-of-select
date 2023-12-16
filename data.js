const memeDetail = {
  'memeDetailID': 'uuid',
  'image': 'url..',
  'content': 'text...'
}

const content = {
  'contentID': 'uuid',
  'title': 'text',
  'voteCount': 10,
}

const user = {
  'userID': 'uuid',
  'username': 'sungjun',
}

const issue = {
  'issueID': 'uuid',
  'userID': user, // TODO..
  'title': 'text',
  'content1': content,
  'content2': content,
  'allVoteCount': 200,
  'createdAt': '2020-01-01 00:00:00',
}

const userDDK = {
  'userDDKID': 'uuid',
  'userID': user,
  'issueID': issue,
}

const meme = {
  "memeID": "uuid",

  "title": "문득....",

  "content1": content,
  "content2": content,

  "primary": memeDetail,
  "secondary": memeDetail,
}



ISSUE_API = {
  'baseURL': '.../issue/',
  'create': {
    type: 'post',
    request: {
      'user_id': 'uuid',
      'title': 'text',
      'content_1': 'text',
      'content_2': 'text'
      }
    },
    response: {
      sucessed: {
        'issue_id': 'uuid',
      },
      failed: {
        'error': 'some message'
      }
    },
    'search': {
    note: 'it can search only one issue',
    type: 'post',
    request: {
      'user_id': 'uuid',
      'issue_id': 'uuid'
    },
    response: {
      sucessed: {
        "issue": {
          "title": "test_get issue",
          "id": "de0bbf18-99ea-4714-983f-a3ad5b4ab6e4",
          "content_1": {
              "id": "54896546-6ac7-4fbc-81d1-f819e4200aa8",
              "title": "test_get content_1",
              "vote_count": 10
          },
          "content_2": {
              "id": "6e5d1281-5d9c-44e4-9087-0ee17db54ee5",
              "title": "test_get content_2",
              "vote_count": 2
          },
          "all_vote_count": 12
        }
      },
      failed: {
        'error': 'some message'
      }
    }
  },
  'search/hot': {
    note: 'it will show hot issue lists : sort by all_vote_count;',
    type: 'get, post', // get -> no filtered, post -> filtered
    request: {
      'user_id': 'uuid'
    },
    response: {
      "issues": [
        {
          "title": "test_get issue",
          "id": "de0bbf18-99ea-4714-983f-a3ad5b4ab6e4",
          "content_1": {
            "id": "54896546-6ac7-4fbc-81d1-f819e4200aa8",
            "title": "test_get content_1",
            "vote_count": 10
          },
          "content_2": {
            "id": "6e5d1281-5d9c-44e4-9087-0ee17db54ee5",
            "title": "test_get content_2",
            "vote_count": 2
          },
          "all_vote_count": 12
        },
        {
          "title": "test_get issue",
          "id": "b0e854fa-46af-4fdc-9d05-537d41ad9913",
          "content_1": {
            "id": "4fd6fb18-fa1e-4c8b-af5b-91b9aa197b29",
            "title": "test_get content_1",
            "vote_count": 0
          },
          "content_2": {
            "id": "fb53a393-308f-4b5e-9d7f-8ef0fb8921c1",
            "title": "test_get content_2",
            "vote_count": 0
          },
          "all_vote_count": 0
        }
      ]
    }
  },
  'search/all': {
    note: 'it will show issue lists : sort by create at;',
    type: 'get, post', // get -> no filtered, post -> filtered
    request: {
      'user_id': 'uuid'
    },
    response: {
      "issues": [
        {
          "title": "test_get issue",
          "id": "de0bbf18-99ea-4714-983f-a3ad5b4ab6e4",
          "content_1": {
            "id": "54896546-6ac7-4fbc-81d1-f819e4200aa8",
            "title": "test_get content_1",
            "vote_count": 10
          },
          "content_2": {
            "id": "6e5d1281-5d9c-44e4-9087-0ee17db54ee5",
            "title": "test_get content_2",
            "vote_count": 2
          },
          "all_vote_count": 12
        },
        {
          "title": "test_get issue",
          "id": "b0e854fa-46af-4fdc-9d05-537d41ad9913",
          "content_1": {
            "id": "4fd6fb18-fa1e-4c8b-af5b-91b9aa197b29",
            "title": "test_get content_1",
            "vote_count": 0
          },
          "content_2": {
            "id": "fb53a393-308f-4b5e-9d7f-8ef0fb8921c1",
            "title": "test_get content_2",
            "vote_count": 0
          },
          "all_vote_count": 0
        }
      ]
    }
  },
  'vote': {
    note: 'it will vote issue',
    type: 'post',
    request: {
      'user_id': 'uuid',
      'issue_id': 'uuid',
      'content_id': 'uuid'
    },
    reponse: {
      "issue": {
        "title": "test_get issue",
        "id": "de0bbf18-99ea-4714-983f-a3ad5b4ab6e4",
        "content_1": {
          "id": "54896546-6ac7-4fbc-81d1-f819e4200aa8",
          "title": "test_get content_1",
          "vote_count": 10
        },
        "content_2": {
          "id": "6e5d1281-5d9c-44e4-9087-0ee17db54ee5",
          "title": "test_get content_2",
          "vote_count": 3
        },
        "all_vote_count": 13
      }
    }
  }
}




console.log(meme)
console.log(issue)


