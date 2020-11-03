package Services;

import Domain.Buket;
import Domain.Order;

import java.util.List;

public interface ShopAPI {
    public List<Buket> getBuketter();
    public List<Order> getAllOrders();
    public Order getOrderById(int id);
    public void saveOrder(Order order);
    public void markOrderAsDone(Order order);
}
