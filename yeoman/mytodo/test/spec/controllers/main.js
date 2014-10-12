'use strict';

describe('Controller: MainCtrl', function () {

  // load the controller's module
  beforeEach(module('mytodoApp'));

  var MainCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MainCtrl = $controller('MainCtrl', {
      $scope: scope
    });
  }));

  it('should have no item to start', function () {
    expect(scope.todos.length).toBe(0);
  });

  it('should add one item to the list', function () {
    scope.todo = "Test addition";
    scope.addTodo();
    expect(scope.todos.length).toBe(1);
  });

  it('should remove one item to the list', function () {
    scope.todo = "Test addition";
    scope.addTodo();
    expect(scope.todos.length).toBe(1);
    scope.removeTodo();
    expect(scope.todos.length).toBe(0);
  });
});
