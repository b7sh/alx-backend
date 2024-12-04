import kue from 'kue'


const queue = kue.createQueue();

const obj = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const queueName = 'push_notification_code';

const job = queue.create(queueName, obj).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`)
})
  .on('complete', () => console.log('Notification job completed'))
  .on('fail',() => console.log('Notification job failed'));
