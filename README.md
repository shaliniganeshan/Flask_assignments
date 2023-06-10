
# Flask Assignment
'''
Address book app by using flask and python
'''
### API Reference

#### Get all items

```http
  GET http://127.0.0.1:9999/show_addresses
```

#### Get item

```http
  GET http://127.0.0.1:9999/show_addresses/<_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Post item

```http
  POST http://127.0.0.1:9999/addresses
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `address`      | `string` | **Required**. Address details  |
| `address_no`      | `int` | **Required**. Door number |
| `latitude`      | `int` | **Required**.  latitude value|
| `longitude`      | `int` | **Required**. longitude value |


#### Put item

```http
  PUT http://127.0.0.1:9999/addresses/<_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
| `address`      | `string` | **Required**. Address details  |
| `address_no`      | `int` | **Required**. Door number |
| `latitude`      | `int` | **Required**.  latitude value|
| `longitude`      | `int` | **Required**. longitude value |

##### which key need to update change that

#### Delete item

```http
  DELETE http://127.0.0.1:9999/addresses/<_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

## Screenshots

![Post methode output](https://github.com/shaliniganeshan/Flask_assignments/blob/master/create_new_add_op.png)

![Get methode output](https://github.com/shaliniganeshan/Flask_assignments/blob/master/show_add_op.png)

![Delete methode output](https://github.com/shaliniganeshan/Flask_assignments/blob/master/del_add_op.png)

## Authors

- [@shaliniganesan](https://github.com/shaliniganeshan)

